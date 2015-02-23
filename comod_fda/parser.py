"""
Must define three methods:

* answer_pattern(pattern, args)
* render_answer_html(answer_data)
* render_answer_json(answer_data)
"""
from .patterns import PATTERNS, FOOD_RECALL_COUNT_PATTERNS, FOOD_RECALL_DETAIL_PATTERNS

import json
import os
import re
import requests
from django.template import loader, Context
from django.conf import settings

# a regular expression so we can find the variables in
# the "blah blah pattern {variable}" patterns
PATTERN_ARGS_RE = re.compile(r'{([A-Za-z0-9_]+)}')


def get_api_key():
    key = None
    try:
        key = settings.SUNLIGHT_API_KEY
    except:
        pass
    if 'FDA_API_KEY' in os.environ:
        key = os.environ['FDA_API_KEY']
    if key == None:
        raise Exception("To use this module, you must have an FDA API Key.")
    else:
        return key

def food_recall_count(food):
    url = 'https://api.fda.gov/food/enforcement.json?api_key=%s&search=reason_for_recall:%s&limit=100' %  (get_api_key(), food)
    resp = requests.get(url)
    return resp.json()

def food_recall_search_by_reason(reason):
    url = 'https://api.fda.gov/food/enforcement.json?api_key=%s&search=reason_for_recall:%s&limit=100' %  (get_api_key(), reason)
    resp = requests.get(url)
    return resp.json()



############################################################
# Pattern-dependent behavior
def answer_pattern(pattern, args):
    """
    Returns a `dict` representing the answer to the given
    pattern & pattern args.
    """
    if pattern not in PATTERNS:
      # not one of our patterns
      return None
    if len(args) != 1:
      # we didn't actually search anything. (if this is a slow API, you can
      # change this to "len(args) < 5" to wait until a certain # of letters
      # are typed in before firing off your search to the API.)
      return None

    if pattern in FOOD_RECALL_COUNT_PATTERNS:
      
      topic = args[0]
    elif pattern in FOOD_RECALL_DETAIL_PATTERNS:
      # We might be looking up via zip code or text search, so see what
      # pattern the user used
      args_keys = PATTERN_ARGS_RE.findall(pattern)
      kwargs = dict(zip(args_keys,args))

      if "reason" in kwargs:
        # a zipcode search
        reason = kwargs['reason']
        return {
          'type': 'food_recall_details',
          'reason': reason,
          'data': food_recall_search_by_reason(reason)
        }

    return None




############################################################
# Applicable module-wide
def render_answer_html(answer_data):
    # This receives what we got in `answer_pattern` and returns HTML.
    if answer_data and answer_data.get('type', None) == "food_recall_details":
      data = answer_data['data']
      template = loader.get_template('comod_fda/food_recall_details.html')
      return template.render(Context(data))
    else:
      # TODO: render a template for "we don't know how to handle this search
      raise Exception

def render_answer_json(answer_data):
    return json.dumps(answer_data)
