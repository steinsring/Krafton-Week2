class Solution:
    def calculate(self, s: str) -> int:
        pass

        # 중위 표기식을 후위 표기식으로 변환하고
        # 후위 표기식을 스택으로 계산한다.

        # 문자열 s를 숫자만 스택에 집어넣고
        # 연산자는 연산자 스택에서 

        # 후위연산자 변환
        priority = {"(" : 1, ")" : 1, "+" : 2, "-" : 2, }

        # 공백제거
        del_blank = ""
        for b in s:
            if b != " ":
                del_blank += b

        # 문자열 파싱
        pre_opperand = ""
        parsing = []
        temp = ""
        for i in range(len(del_blank)):
            if del_blank[i].isalnum():
                temp += del_blank[i]
            else:
                # 앞에 피연산자가 없는 단항 "-"
                if temp == "" and del_blank[i] == "-" and pre_opperand != ")":
                    parsing.append("0")
                    parsing.append(del_blank[i])
                    pre_opperand = del_blank[i]
                    continue

                if temp != "":
                    parsing.append(temp)
                parsing.append(del_blank[i])
                pre_opperand = del_blank[i]
                temp = ""

        # 파싱하고 남은거 처리
        if temp != "":
            parsing.append(temp)



        # 후위 연산자 변환
        post_fix = []
        stack = []
        for output in parsing:
            if output.isalnum():
                post_fix.append(output)
                continue

            if output == " " or output == '':
                continue

            if not stack:
                stack.append(output)
                continue

            # 괄호시작 이거나 연산자라면 스택에 추가
            if output == "(" or stack[-1] == "(" and output != ")":
                stack.append(output)
            # 닫는 괄호라면 여는 괄호가 나올때까지 연산자를 출력
            elif output == ")":
                p = stack.pop()
                while p != "(":
                    post_fix.append(p)
                    p = stack.pop()

            else:   # 여기서 우선순위 비교
                if priority[stack[-1]] <= priority[output]:
                    # (가 나올때까지 우선순위 비교하면서 pop
                    while stack and stack[-1] != "(" and priority[stack[-1]] <= priority[output]:
                        post_fix.append(stack.pop())
                    stack.append(output)
                else:
                    stack.append(output)

        # 남은거 추가
        while stack:
            post_fix.append(stack.pop())

        # 숫자가 1개면 그냥 출력
        if len(post_fix) == 1:
            return int(post_fix[0])
        
        #post fix 계산기
        for output in post_fix:
            if output.isalnum():
                stack.append(int(output))
                continue

            operand1 = int(stack.pop())
            operand2 = int(stack.pop())

            if output == "+":
                result = operand2 + operand1
            else:
                result = operand2 - operand1    # 순서

            stack.append(result)

        return stack[0]
            



if __name__ == "__main__":
    a = Solution()

    list1 ="-2+ 1"
    # s = "ABCCED"
    print(a.calculate(list1))