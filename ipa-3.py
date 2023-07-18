#!/usr/bin/env python
# coding: utf-8

# In[43]:


'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    following = False #if from member is following to member
    followed = False #if to member is following from member
    
    for person in (social_graph[from_member]['following']):
        if person == to_member:
            following = True
            break
        else:
            following = False
            
    for person in (social_graph[to_member]['following']):
        if person == from_member:
            followed = True
            break
        else:
            followed = False
            
    if following==True and followed==True:
        status = "friends"
        
    elif following==True and followed==False:
        status = "follower"
        
    elif following==False and followed==True:
        status = "followed by"
        
    else:
        status = "no relationship"
        
    return(status)


# In[44]:


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    size = len(board)
    chars = []
    winner = None
    
    for i in board:
        for j in i:
            chars.append(j)
    uniqueChar = list(set(chars)) 
    #to get what symbols are used
    
    #row check
    for i in board :
        if len(set(i)) == 1 :
            winner = i[0]
            break
            
    #column related
    colCount = 0
    col = []
    while colCount <= size - 1 :
        for i in board:
            col.append(i[colCount])
        colCount += 1
    
    colList = []
    for i in range(0,len(col),size):
        colList.append(col[i:i+size])
    
    for i in colList :
            if len(set(i)) == 1 :
                winner = i[0]
                break
                
    # diagonals check
    diag = []
    Ldiag = []
    Rdiag = []
    
    Lcount = 0
    for i in board:
        Ldiag.append(i[Lcount])
        Lcount += 1
    diag.append(Ldiag)

    Rcount = size - 1
    for i in board:
        Rdiag.append(i[Rcount])
        Rcount -= 1
    diag.append(Rdiag)

    for i in diag :
            if len(set(i)) == 1 :
                winner = i[0]
                break

    if winner == None or winner == '':
        return "NO WINNER"
    else :
        return winner
    


# In[45]:


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    try:
        return(route_map[first_stop, second_stop]["travel_time_mins"])
    except:

        for route in route_map:
            if route[0] == first_stop:
                index1 = list(route_map).index(route)

        for route in route_map:
            if route[1] == second_stop:
                index2 = list(route_map).index(route)

        routing = list(dict.keys(route_map))

        tolTime = 0
        while (index1 % len(routing) != index2):
            startKey = routing[index1 % len(routing)]
            tolTime += route_map[startKey]["travel_time_mins"]
            index1 += 1

        if(index1 >= len(routing)):
            tolTime += route_map[routing[index1 % len(routing)]]["travel_time_mins"]
        else:
            tolTime += route_map[routing[index1]]["travel_time_mins"]

    return(tolTime)

