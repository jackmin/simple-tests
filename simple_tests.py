#!/usr/bin/env python3

from pexpect import pxssh
from pexpect import TIMEOUT
from testpmd import testpmd_exec
from importlib import import_module
import sys
import argparse

def run():
    im=import_module(name=f'cases.{args.module_name}')
    tests=im.tests
    server=im.server
    workdir=im.workdir
    cmd=im.cmd
    s=pxssh.pxssh(encoding='utf-8')
    s.echo=False
    #s.logfile=sys.stdout
    s.login(username='jackmin', server=server)
    s.set_unique_prompt()
    s.prompt()
    s.sendline('sudo ip link add dummy0 type dummy; sudo ip link set dummy0 up')
    s.prompt()
    s.sendline('cd ' + workdir)
    s.prompt()
    s.sendline(cmd)
    s.expect('testpmd>')
    s.sendline('flow flush 0')
    s.expect('testpmd>')
    s.timeout=2
    i = 0
    for t in tests:
        result = testpmd_exec(s, t[0], t[1])
        if not result:
            print(f'NOK:\n>>>{t[0]}\n|||{t[1]}\n<<<{s.before.strip()}')
        else:
            print(f'{i}/{len(tests)} OK: {t[0]}')
        i = i + 1
    s.interact()
    s.sendline('quit')
    s.prompt()
    s.logout()
    s.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('module_name')
    args = parser.parse_args()
    run()
