class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email=set()
        for i in emails:
            local,domain=i.split("@")
            e=""
            for j in local:
                if j=="+" or j=="-":
                    break
                if j.isalnum():
                    e+=j
            email.add(e+"@"+domain)
        return len(email)

