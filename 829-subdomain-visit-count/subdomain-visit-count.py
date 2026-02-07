class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        visit_count  = {
            
        }
        for i in cpdomains:
            count , domains = i.split(' ')
            subdomain =  domains.split('.')
            for j in range(len(subdomain)): 
                sub = '.'.join(subdomain[j:])
                if sub in visit_count:
                    visit_count[sub] += int(count)
                else:
                    visit_count[sub] = int(count)

        answer = []
        for key in visit_count:
            temp = str(visit_count[key]) + " " + key
            answer.append(temp)
        
        return answer
        