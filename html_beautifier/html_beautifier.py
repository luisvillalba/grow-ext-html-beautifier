"""Html pretty print extension Grow sites."""

from bs4 import BeautifulSoup as bs
import html5lib
import re
import sys
from grow import extensions
from grow.pods import errors
from grow.extensions import hooks
from grow.documents import document

r = re.compile(r'^(\s*)', re.MULTILINE)

class BeautifyPostRenderHook(hooks.PostRenderHook):
  """Handle the post-render hook."""

  def trigger(self, previous_result, doc, raw_content, *_args, **_kwargs):
    """Execute post-render modification."""
    parser = None
    formatted = ''

    try:
      if not doc.view.endswith('.html'):
        return previous_result
    except Exception:
      return previous_result

    self.set_config(self.extension.config.get('options', {}))
    content = previous_result if previous_result else raw_content

    if self.config['trigger'] and not doc.fields.get('html_beautify'):
      return previous_result

    if self.config['strict_validation']:
      try:
        parser = html5lib.HTMLParser(strict=True)
        parser.parse(content)
        formatted = bs(content, 'html.parser').prettify(formatter='html')
      except html5lib.html5parser.ParseError:
        print 'ERROR'
        for pos, code, datavars in parser.errors:
          print 'HTML validation error in line {} col {}'.format(pos[0], pos[1])
          print html5lib.constants.E.get(code, 'Unknown error "%s"' % code) % datavars
          print content.split('\n')[pos[0] - 2]
          print content.split('\n')[pos[0] - 1]
          print content.split('\n')[pos[0]]
          print content.split('\n')[pos[0] + 1]
        raise Exception
    else:
      formatted = bs(content, 'html.parser').prettify(formatter='html')

    return r.sub(r'\1' * self.config['tab_size'], formatted)

  def set_config(self, options):
    self.config = {}
    self.config['tab_size'] = options.get('tab_size', 2)
    self.config['strict_validation'] = options.get('strict_validation', True)
    self.config['trigger'] = options.get('trigger', False)


class HtmlBeautifierExtension(extensions.BaseExtension):
  """HTML Beautifier Grow extension."""

  @property
  def available_hooks(self):
    """Returns the available hook classes."""
    return [BeautifyPostRenderHook]
