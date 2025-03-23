"""
members: {
    회원: [추천인, 총수익]
}
"""
def process(members, member, income):
    if member == "-": return
    if income == 0: return
    
    payout = int(income * 0.1)
    income -= payout
    members[member][1] += income
    process(members, members[member][0], payout)
    
def solution(enroll, referral, seller, amount):
    members = {
        member: [referral[i], 0]
        for i, member in enumerate(enroll)
    }
    for i, member in enumerate(seller):
        payout = int((amount[i] * 100) * 0.1)
        income = amount[i] * 100 - payout
        members[member][1] += income
        
        process(members, members[member][0], payout)
    return [members[member][1] for member in enroll]