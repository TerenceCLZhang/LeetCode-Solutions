class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        writer = reader = 0

        curr_char = None
        curr_count = 0

        while reader < n:
            c = chars[reader]
            reader += 1

            if c == curr_char:
                curr_count += 1
            else:
                if curr_char is not None:
                    chars[writer] = curr_char
                    writer += 1

                    if curr_count > 1:
                        for d in str(curr_count):
                            chars[writer] = d
                            writer += 1

                curr_char = c
                curr_count = 1

        if curr_char is not None:
            chars[writer] = curr_char
            writer += 1

            if curr_count > 1:
                for d in str(curr_count):
                    chars[writer] = d
                    writer += 1

        return writer
