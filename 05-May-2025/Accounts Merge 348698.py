# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        mp={} #email to name map

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)


        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                union(email, first_email)
                mp[email] = name
        
        roots = defaultdict(list)

        for email in parent:
            root = find(email)
            roots[root].append(email)
        
        ans=[]
        for root, email in roots.items():
            name = mp[root]
            ans.append([name] + sorted(email))
        return ans

