using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameControllerScript : MonoBehaviour
{
    int nRounds = 5;
    int time = 10;

    string player1nick;
    string player2nick;

    bool p2Joined = false;
    bool timeUp = false;

    private int code;

    int player1points;
    int player2points;

    int player1TotalPoints;
    int player2TotalPoints;

    void StartGame()
    {
        if(!p2Joined && timeUp)
        {
            player1points = 0;
            player2points = 0;
            player1TotalPoints = 0;
            player2TotalPoints = 0;
            //TODO
        }
    }

    public void SendTimesUp()
    {
        timeUp = true;
    }

    void StartRound()
    {
        player1points = 0;
        player2points = 0;
        //TODO
    }

    public void GetCodeInput(string s)
    {
        int.TryParse(s, out code);
        Debug.Log(code);
    }

    public void JoinGame()
    {
        if (code != 0)
        {

        }
        //TODO
    }

    void EndRound()
    {
        Debug.Log(player1nick + "(P1): " + player1points);
        Debug.Log(player2nick + "(P2): " + player2points);
        player1TotalPoints += player1points;
        player2TotalPoints += player2points;
        //TODO
    }

    public void SetRounds(int n)
    {
        nRounds = n;
        Debug.Log("rounds: " + nRounds);
    }

    public void SetTime(int t)
    {
        time = t;
        Debug.Log("time: " + time);
    }
}
