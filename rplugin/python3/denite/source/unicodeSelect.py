#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import Base

import os.path

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'unicodeSelect'
        self.kind = 'word'

    def gather_candidates(self, context):
        data_path = self.vim.eval('g:denite_unicode_data_path')
        codeset = context['args'][0]
        codeset_file = os.path.join(data_path, codeset + '.txt')

        if not os.path.isfile(codeset_file):
            self.vim.out_write('"{}" not found!\n'.format(codeset_file))
            return []

        with open(codeset_file) as f:
            return [
                {
                    'word' : line,
                    'action__text' : line.split(';')[0],
                }
                for line in f
                if ';' in line
            ]

