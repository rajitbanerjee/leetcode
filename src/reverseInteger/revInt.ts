// reverse a 32-bit signed integer; return 0 if reversal goes outside range
function reverse(x: number): number {
  const digits: string = String(x).substring(x < 0 ? 1 : 0);
  const rev: number = parseInt(digits.split("").reverse().join(""), 10);

  const is32BitInt = (n: number): boolean => n >= -(2 ** 31) && n <= 2 ** 31 - 1;
  const fixSign = (x: number, rev: number): number => (x < 0 ? -rev : rev);

  return is32BitInt(rev) ? fixSign(x, rev) : 0;
}

function test(x: number): void {
  console.log(`Input: ${x}\nOutput: ${reverse(x)}\n`);
}

test(123);
test(-123);
test(120);
test(0);
test(1534236469);
