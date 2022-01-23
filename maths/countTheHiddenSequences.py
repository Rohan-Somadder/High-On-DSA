# https://leetcode.com/problems/count-the-hidden-sequences/
# Solution:  https://leetcode.com/problems/count-the-hidden-sequences/discuss/1709755/JavaC%2B%2BPython-Straight-Forward-Solution-with-Explantion
# Solution : https://www.youtube.com/watch?v=Le0YmVPhdu4 (watch this)

class Solution(object):
    
    # TC : O(N^2)
    # SC : O(1)
    # Brute Force Approach : TLE
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]8
        :type lower: int
        :type upper: int
        :rtype: int
        """
        count = 0
        i = lower

        for i in range(lower, upper+1):
            for j in range(len(differences)):
                if i+differences[j] < lower or i+differences[j] > upper:
                    break
                else:
                    i += differences[j]
                
                if j == len(differences)-1:
                    count += 1
                    
        return count

    

    # TC : O(N)
    # SC : O(1)
    
    def numberOfArraysApproach2(self, differences, lower, upper): 
        
        # Variable to store the result
        total_sequences = 0
        
        # Now we will be creating a possible sequence starting from lower bound
        sequence = [lower] 
        
        for j in range(len(differences)):
            x = sequence[j] + differences[j]
            sequence.append(x)
        
        # sequence array will have a possible sequence at lower bound
        # we will extract the minimum and maximum value from this sequence array
        
        minn, maxx = min(sequence), max(sequence)
        
        # then we will do one edge check
        if lower <= minn <= upper and lower <= maxx <= upper: total_sequences += 1
            
        # then we will check in range of lower and upper bound if min and max are range or not
        # obviously the place where we find min and max will also be the place where we will find extreme min and max for i in lower and upper bound
        # when we increase lower and upper by one we increase minn and maxx also because of they will have same differences
        
        for i in range(lower + 1, upper+1):
            minn = minn + 1
            maxx = maxx + 1
            
            # here we just check that our minn and maxx which are extreme are still in bounds or not
            # if they are in bound we increment our result
            if lower <= minn <= upper and lower <= maxx <= upper: total_sequences += 1
            
        return total_sequences

    # TC : O(N)
    # SC : O(1)
    # Most Efficient Approach
    
    # Runtime: 1264 ms, faster than 100.00% of Python3 online submissions for Count the Hidden Sequences.
    # Memory Usage: 29.4 MB, less than 16.67% of Python3 online submissions for Count the Hidden Sequences.
    def numberOfArraysApproach3(self, differences, lower, upper):
        """
        :type differences: List[int]8
        :type lower: int
        :type upper: int
        :rtype: int
        """
        
        minimumInSequence = 0
        maximumInSequence = 0
        
        a = 0
        for i in differences:
            a+=i
            minimumInSequence = min(minimumInSequence, a)
            maximumInSequence = max(maximumInSequence, a)
        
        lowerBoundAllowed = lower - minimumInSequence
        upperBoundAllowed = upper - maximumInSequence
        
        return max(0, upperBoundAllowed - lowerBoundAllowed + 1)
        
        
    # TC : O(N)
    # SC : O(1)
    # Most Efficient Approach
    # In python 3 of leetcode this will work
    
    # def numberOfArrays(self, differences, lower, upper):
        # A = list(accumulate(differences, initial = 0))
        # return max(0, (upper - lower) - (max(A) - min(A)) + 1)
        

    

print(Solution().numberOfArrays([1, -3, 4], 1, 6))
print(Solution().numberOfArrays([3,-4,5,1,-2], -4,5))
print(Solution().numberOfArrays([4,-7,2], 4,5))
print(Solution().numberOfArrays([-40], -46,53))
print(Solution().numberOfArrays([41881,325,-49749,49627,6212,-29381,-49282,33522,32510,-17919,-7523,-39820,6760,-16868,8017,23872,-37943,26382,12313,-28327,25958,-4104,-8625,39628,-14532,41093,-18299,-45808,11388,43215,12394,-38019,38715,-38023,-1743,22791,-23638,22499,-39236,5016,5308,13814,-32084,258,-18174,16388,23791,9697,31993,-43412,16924,-23396,-38112,17227,-25021,26205,31064,32753,-23016,8986,10953,-21704,11376,-35400,26552,-33136,40183,3904,-6771,-26296,41356,6695,-32475,-4211,36141,-35958,-8734,23023,-20496,-3992,-16389,860,27004,-49980,34023,10504,-6239,32106,-10160,-43886,-1583,24012,-24743,23619,-40118,10515,-11945,38672,7766,-38217,40812,43935,-14798,379,1272,1112,3185,-31408,30867,-23910,-42522,-1447,6029,-22880,17733,6078,42266,-15628,24985,16310,-566,-5588,-13140,23267,-36477,2428,-13047,-14644,17083,10462,-28903,43168,-31646,-1568,-30610,25471,39608,3357,-44069,6498,5918,-3711,-13746,-22553,10598,14745,4099,21652,-38751,-1720,-10938,-3157,24721,19057,-15807,-8149,31326,-45474,38380,-15281,2644,36423,-21657,-25883,31324,35093,-5309,8191,-35327,-22749,-36249,40475,7432,-29269,42122,-36929,18710,-24671,-8250,15780,30183,32432,-17584,-23051,1468,-25124,34675,-14487,26627,13365,-46271,-34001,4660,34740,49680,-16167,-2262,3791,-47454,11907,5649,36164,-2477,-44082,-32735,17384,-26495,48829,-29617,-16935,4928,20882,40855,-8587,-37936,-10064,-6801,12026,-9983,15828,-19385,14525,20838,-2740,-14927,3268,35268,-32411,30532,-43456,-5346,-5930,36037,-3325,-2662,27746,-10868,24638,-33011,34742,-6773,7714,18971,-2775,-41695,30228,-28283,-27117,8178,25638,12086,20422,-9314,-49719,7550,-39662,49277,-19747,14218,-36328,12794,-403,10538,32169,2716,26388,-20286,17749,6925,-24461,571,-42100,27945,3320,-1255,-7011,5381,12384,-48149,47047,4075,1491,-2207,-4771,20495,-47057,8305,-25878,22245,-16666,4409,5919,-28710,34448,4039,37193,-12467,-43798,-25515,47557,-49898,-948,46007,-12268,37852,-41115,-14648,-11313,-1204,33129,24356,-12083,-48297,46533,-39424,13962,11740,-4190,-10355,8588,9088,31741,-12602,15204,-3161,-15075,39399,-14838,-26792,-28346,-13133,47499,24398,-7860,-67,1176,-43989,-12271,11252,13051,-27560,-15019,10137,11139,8212,-24827,23303,-15543,-8361,20778,27948,35744,-13712,-33064,-42248,9992,22988,-24461,3538,39722,13026,-43987,-4047,3180,7066,19140,17098,-12192,7612,-44640,36795,24494,-32427,-12977,29080,-29153,26068,-47655,44186,-17626,-3432,48260,-35923,-440,-26412,25065,41446,-42111,38457,12146,-9317,-736,1955,3674,-23975,31066,-3037,-41769,-32537,-3670,9908,-14113,5258,36011,10239,17286,-18874,-36951,16830,19976,-24746,-34356,32891,25174,-33,31773,2575,-23990,-19068,-35023,47283,897,31932,-30165,-29287,-12555,-16324,47742,31133,-40939,-17282,9198,-21949,-8830,7947,2685,46012,7889,26670,-30609,-49080,11894,-32078,14198,-21,21533,-11509,-1920,-11196,3760,34258,-8103,-26933,30672,47378,-44551,12177,-10819,41529,-2223,-17417,-9843,5767,24859,-14768,-49433,-1463,-8386,21795,-13298,38535,8630,-1078,-37314,37136,-35942,41326,3054,-41091,1155,-38940,44880,-24920,34952,38356,-30463,32007,-35725,-42032,5092,35574,22410,-20507,31064],-49929,80366))

