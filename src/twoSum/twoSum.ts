function twoSum(nums: number[], target: number): number[] {
  let seen: Map<number, number> = new Map();
  for (const [i, num] of nums.entries()) {
    const complement: number = target - num;
    if (seen.has(complement)) {
      return [seen.get(complement)!, i];
    }
    seen.set(num, i);
  }
  return [-1, -1];
}

// test
const nums: number[] = [2, 7, 11, 15];
const target: number = 9;
console.log(`Input: nums = ${nums}, target = ${target}`);
console.log(`Output: ${twoSum(nums, target)}`);
