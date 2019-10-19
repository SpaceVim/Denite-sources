#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import Base

import glob
import os.path

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'unicode'
        self.kind = 'source'

    def gather_candidates(self, context):
        data_path = self.vim.eval('g:denite_unicode_data_path')

        if not os.path.isdir(data_path):
            self.vim.out_write('g:denite_unicode_data_path "{}" not exists!\n'.format(data_path))
            return []

        return [
            {
                'word': codeset,
                'kind': 'source',
                'action__source': ['unicodeSelect', codeset],
            }
            for codeset in sorted([
                os.path.splitext(os.path.basename(p))[0]
                for p in glob.glob(os.path.join(data_path, '*.txt'), recursive=False)
            ])
        ]
