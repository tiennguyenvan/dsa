class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        cur_len = 0
        stack = []
        for w in words:
            # total len in stack + stack len + cur w <= maxWidth => go
            # otherwise, process
            if cur_len + len(stack) + len(w) <= maxWidth:
                stack.append(w)
                cur_len += len(w)
                continue
            line = []
            if len(stack) == 1:
                line = [stack[0], ' ' * (maxWidth - len(stack[0]))]
            else:
                spaces = [0] * (len(stack) - 1)
                cur_space_i = 0
                while cur_len < maxWidth:
                    spaces[cur_space_i] += 1
                    cur_len += 1
                    cur_space_i = (cur_space_i + 1) % len(spaces)
                spaces.append(0)
                for i in range(len(stack)):
                    line.append(stack[i])
                    line.append(' ' * spaces[i])

            lines.append(''.join(line))

            stack = [w]
            cur_len = len(w)

        right_spaces_needed = maxWidth - (len(stack) - 1 + cur_len)
        if right_spaces_needed:
            stack.append(' ' * (right_spaces_needed - 1))
        lines.append(' '.join(stack))

        return lines
