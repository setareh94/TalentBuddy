def solution(A):
	N = len(A)
	total = sum(A)
	lefts = 0
	for p, value in enumerate(A):
		partial = total - value
		if partial % 2 == 0 and lefts == (partial / 2) and 0 <= p < N:
			return p
		lefts += value
	return -1


def solution(A):

	if len(A) == 0:
		return -1

	result = []
	sum_before = 0
	sum_after = sum(A[0:])


	sum_after -= A[0]

	if sum_before == sum_after:
		result.append(0)
	for i in xrange(1,len(A)): 
		sum_before += A[i-1]
		sum_after -= A[i]

		if sum_before == sum_after:
			result.append(i)

	if not(result):
		return -1
	else:
	return result[0]

def solution(A):
	if A:
		n=len(A)
	if n>1:
		s1=0	
		s2=sum(A)
	for i,e in enumerate(A):
		if s1==(s2-e):
			return i
		s1+=e
		s2-=e
	return -1
		else:
			return 0
	return -1
