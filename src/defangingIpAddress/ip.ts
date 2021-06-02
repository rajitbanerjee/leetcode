function defangIPaddr(address: string): string {
  return address.replace(/\./g, "[.]");
}

// test
const address = "1.1.1.1";
console.log(`Input: address = ${address}`);
console.log(`Output: ${defangIPaddr(address)}`);
