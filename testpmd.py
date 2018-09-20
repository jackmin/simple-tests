from pexpect import TIMEOUT

def testpmd_exec(testpmd, cmd_str, result):
    testpmd.sendline(cmd_str)
    testpmd.expect(cmd_str)
    idx = testpmd.expect([result, TIMEOUT])
    testpmd.expect('testpmd>')
    return False if idx else True
