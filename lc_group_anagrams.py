# https://neetcode.io/solutions/group-anagrams

# my origional solution
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        dict_char = {}
        dict_str = {}
        for char in "abcdefghijklmnopqrstuvwxyz" :
            dict_char[char] = 0
        for index, each in enumerate(strs):
            dict_char_copy = dict_char.copy()
            count = 25
            dict_str[(each, index)] = 0
            for char in each:
                dict_char_copy[char] += 1
            for num in dict_char_copy.values():
                dict_str[(each, index)] += num*(2**count)
                count -= 1
        grouped = {}
        for (each, index), value in dict_str.items():
            if value not in grouped:
                grouped[value] = [each]
            else:
                grouped[value].append(each)
        for value in grouped.values():
            result.append(value)
        
        return result


# chatgpt modifed solution
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        dict_char = {}
        dict_str = {}

        # Initialize a dictionary to count characters
        for char in "abcdefghijklmnopqrstuvwxyz":
            dict_char[char] = 0

        # Process each string in the input list
        for index, each in enumerate(strs):  # Use the index to handle duplicates
            dict_char_copy = dict_char.copy()
            count = 25
            dict_str[(each, index)] = 0  # Unique key for duplicate strings

            # Count characters in the current string
            for char in each:
                dict_char_copy[char] += 1

            # Create a unique signature for each string
            for num in dict_char_copy.values():
                dict_str[(each, index)] += num * (2 ** count)
                count -= 1

        # Group strings based on their unique signatures
        grouped = {}
        for (key_word, _), value in dict_str.items():
            if value not in grouped:
                grouped[value] = [key_word]
            else:
                grouped[value].append(key_word)

        # Prepare and sort the result
        result = list(grouped.values())

        return result




# slimpler solution
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grouped = {}

        # Group words by their character count signature
        for word in strs:
            # Create a tuple of character counts (26 slots for 'a' to 'z')
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1

            # Convert the count list to a tuple, which is hashable
            signature = tuple(count)

            # Add the word to the corresponding group
            if signature not in grouped:
                grouped[signature] = [word]
            else:
                grouped[signature].append(word)

        # Return the grouped anagrams as a list of lists
        return list(grouped.values())
