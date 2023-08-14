import logging


class CONFIG:
    log_level = logging.DEBUG

    source = "/Users/cong.zhang/PycharmProjects/solidity-supplychain-checker/testcases/Centurion/CIX.sol"
    # source = "/Users/cong.zhang/dev/tests/Challenges/demo3.sol"
    # source = "/Users/cong.zhang/dev/tests/Challenges/2/Lender.sol"
    dist = "/Users/cong.zhang/dev/CodeQL-For-Solidity/test"
    builtins = "/Users/cong.zhang/dev/CodeQL-For-Solidity/src/ast2java/builtins"
