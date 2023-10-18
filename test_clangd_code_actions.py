#
# Run with: python3 test_clangd_code_actions.py "/path/to/clangd --compile-commands-dir=./code-actions-test --log=verbose"
#

import ls_interact as ls
from common import JsonRpc
import os


def interact(json_rpc):

    paths = ['./code-actions-test/test_clangd_code_actions.c']

    for p in paths:
        json_rpc.notify(ls.DidOpenTextDocument(p))

    for p in paths:
        json_rpc.wait_for(JsonRpc.JsonRpcPendingMethod(
            'textDocument/publishDiagnostics'))
    r = json_rpc.request(ls.CodeAction(paths[0], ls.Range(4, 13, 4, 13), []))
    r = json_rpc.wait_for(r)


def main():
    ls.run(interact)


if __name__ == '__main__':
    main()
