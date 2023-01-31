*** Settings ***

*** Test Cases ***
testtmp
  ${a}  create dictionary  a=1  b=2
  log many  ${a}