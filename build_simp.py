#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from opencc import OpenCC

converter = OpenCC('t2s.json')

with open('luna_pinyin.dict.yaml') as f, open('luna_pinyin_simp_native.dict.yaml', 'w') as g:
    # Header
    for line in f:
        if line != '...\n':
            # Override several configurations
            if line == 'name: luna_pinyin\n':
                g.write('name: luna_pinyin_simp_native\n')
            elif line == 'use_preset_vocabulary: true\n':
                g.write('vocabulary: essay-zh-hans\n')
            else:
                g.write(line)
        else:
            g.write('...\n')
            break

    # Dictionary
    for line in f:
        g.write(converter.convert(line))
