import matplotlib.pyplot as plt
import matplotlib.scale as scale
import leaderboardUtils

# Set some colors
aocText = "#CCCCCC"
aocBackground = "#0F0F23"
aocGold = "#FFFF66"
aocSilver = "#9999CC"

# Set background color
fig = plt.figure()
fig.patch.set_facecolor(aocBackground)

# Do some of the styling
with plt.rc_context( {"axes.edgecolor":aocText, "xtick.color":aocText, "ytick.color":aocText, "figure.facecolor":aocBackground, "axes.facecolor":aocBackground} ):

    # These variables will get set to some values via scraping the info from the leaderboard in a future update
    days = [1, 2, 3, 4, 5, 6]
    goldStars = [114000, 96000, 79000, 63000, 55000, 48000]
    silverStars = [7600, 2600, 2400, 8000, 1100, 1950]

    leaderboard = leaderboardUtils.getLeaderboard()
    #print( leaderboard)
    days = []
    for item in leaderboard:
        days.append( int(item[0]))
    
    goldStars = []
    for item in leaderboard:
        goldStars.append( int(item[1]))

    silverStars = []
    for item in leaderboard:
        silverStars.append( int(item[2]))

    print(days)
    print(goldStars)
    print(silverStars)
    
    # plot the data with corresponding color.
    plt.plot( days, goldStars, aocGold, label="Gold Stars (Both puzzles completed)", marker="*")
    plt.plot( days, silverStars, aocSilver, label="Silver Stars (One puzzle completed)",  marker="*")
    
    #label axes and make them white
    plt.ylabel( "Users", color = aocText)
    plt.xlabel( "Day", color = aocText)

    # set axis limits and steps
    #plt.axis([days[0], days[len(days) - 1], sorted(silverStars)[0], sorted(goldStars)[len(goldStars) - 1]])
    #plt.xlim(0, sorted(goldStars)[len(goldStars) - 1])
    #plt.ylim(1, days[len(days) - 1])
    
    #plt.yscale = scale.LinearScale
    #plt.xscale = scale.LinearScale


    # Make legend with white text
    leg = plt.legend( loc="upper right")
    for text in leg.get_texts():
        plt.setp( text, color = aocText)

    # increase the border size
    plt.tight_layout()


# I don"t know why I"m even commenting this part.
plt.show()
