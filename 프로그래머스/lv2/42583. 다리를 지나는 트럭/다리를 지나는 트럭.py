def solution(bridge_length, weight, truck_weights):
    bridge = []
    bridge_time = []
    answer = 0
    while truck_weights or bridge:
        #bridge에추가할 수 있는 조건
        if truck_weights and (sum(bridge)+truck_weights[0] <= weight):
            bridge.append(truck_weights[0])
            bridge_time.append(0)
            truck_weights.pop(0)
        bridge_time = [x+1 for x in bridge_time]
        #bridge에 있다면 finish로
        if bridge and bridge_time[0]==bridge_length:
            bridge.pop(0)
            bridge_time.pop(0)
        answer = answer+1
    return answer+1
