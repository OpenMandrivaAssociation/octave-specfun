#!/bin/sh
curl https://octave.sourceforge.io/specfun/index.html 2>/dev/null | grep -A1 "<dt>Version</dt>" |sed -ne 's,</dd>.*,,;s,.*<dd>,,p'

