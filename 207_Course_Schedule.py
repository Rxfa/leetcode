class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = { i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            prereqs[course].append(pre)
            
        visit_set = set()
        def dfs(course):
            if course in visit_set:
                return False
            if not prereqs[course]:
                return True

            visit_set.add(course)
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            visit_set.remove(course)
            prereqs[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
