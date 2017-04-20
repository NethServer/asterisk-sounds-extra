# asterisk-sounds-extra
NethServer RPM for asterisk-sounds-extra
Based on Sangoma source RPM

## How to build
```
make-srpm asterisk-sounds-extra.spec
srpm=$(basename "$(grep '^Wrote: ' build.log | tail -1 )")
mock -D "dist .ns7" --resultdir=. -r nethserver-7-x86_64 $srpm
```
