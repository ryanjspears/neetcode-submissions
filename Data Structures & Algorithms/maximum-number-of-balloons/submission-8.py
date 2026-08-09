class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        def buildHash(word):
            m = {}
            for l in word:
                if l in m:
                    m[l] += 1
                else:
                    m[l] = 1

            return m


        b = buildHash("balloon")
        t = buildHash(text)

        count = 0
        done = True
        while done:
            #deincrement loop
            for key, value in b.items():
                if key not in t:
                    return count
                    break
                elif t[key] < value:
                    print("hit")
                    return count
                    done = False
                    break
                else:
                    t[key] -= value

            
            count+=1


        return count

