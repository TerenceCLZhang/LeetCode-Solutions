class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        window_start, window_end = -1, -1
        min_length = float("inf")

        t_counter = Counter(t)
        window = {}

        have, need = 0, len(t_counter)
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in t_counter and window[c] == t_counter[c]:
                have += 1

            while have == need:
                curr_window_length = right - left + 1
                if curr_window_length < min_length:
                    window_start, window_end = left, right
                    min_length = curr_window_length

                window[s[left]] -= 1
                if s[left] in t_counter and window[s[left]] < t_counter[s[left]]:
                    have -= 1

                left += 1

        return s[window_start:window_end + 1] if min_length != float("inf") else ""
