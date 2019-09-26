// 205. Isomorphic Strings

// Given two strings s and t, determine if they are isomorphic.

// Two strings are isomorphic if the characters in s can be replaced to get t.

// All occurrences of a character must be replaced with another character while preserving the order of characters.No two characters may map to the same character but a character may map to itself.

//   Example 1:

// Input: s = "egg", t = "add"
// Output: true
// Example 2:

// Input: s = "foo", t = "bar"
// Output: false
// Example 3:

// Input: s = "paper", t = "title"
// Output: true
// Note:
// You may assume both s and t have the same length.

var isIsomorphic = function (s, t) {
  // if strings are of different length
  // they are not isomorphic by definition
  // they have different characters
  if (s.length !== t.length) {
    return false;
  }

  // creating objects that will match
  // characters from one string to the second
  // to keep track of what one letter should shift to
  const firstMatch = {};
  const secondMatch = {};

  for (let idx = 0; idx < s.length; idx += 1) {
    let firstChar = s[idx];
    let secondChar = t[idx];

    // if we are looping on a new character
    // keep track of new character in object
    if (!firstMatch[firstChar]) {
      firstMatch[firstChar] = secondChar;
    } else if (firstMatch[firstChar] !== secondChar) {
      // if the letter we have already matched
      // now matches a different letter than the one in the obj
      // strings are not isomorphic
      return false;
    }

    // same for second obj and string
    if (!secondMatch[secondChar]) {
      secondMatch[secondChar] = firstChar;
    } else if (secondMatch[secondChar] !== firstChar) {
      return false;
    }
  }
  return true;
};


