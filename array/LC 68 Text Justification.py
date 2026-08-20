class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        lines = []
        cur_len = 0
        stack = []
        for w in words:
            # total len in stack + stack len + cur w <= maxWidth => go
            # otherwise, process
            n = len(stack)
            if cur_len + n + len(w) <= max_width:
                stack.append(w)
                cur_len += len(w)
                continue
            line = []
            if n == 1:
                line = [stack[0], " " * (max_width - len(stack[0]))]
            else:
                gap_no = n - 1
                total_spaces = max_width - cur_len
                base, no_w_extra = divmod(total_spaces, gap_no)
                for i in range(n):
                    line.append(stack[i])
                    if i >= gap_no:
                        continue
                    line.append(" " * (base + (1 if i < no_w_extra else 0)))

            lines.append("".join(line))

            stack = [w]
            cur_len = len(w)

        right_spaces_needed = max_width - (len(stack) - 1 + cur_len)
        if right_spaces_needed:
            stack.append(" " * (right_spaces_needed - 1))
        lines.append(" ".join(stack))

        return lines
