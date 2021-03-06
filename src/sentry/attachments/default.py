"""
sentry.attachments.default
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010-2014 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from __future__ import absolute_import

from sentry.cache import default_cache

from .base import BaseAttachmentCache


class DefaultAttachmentCache(BaseAttachmentCache):
    def __init__(self, **options):
        super(DefaultAttachmentCache, self).__init__(default_cache, **options)
