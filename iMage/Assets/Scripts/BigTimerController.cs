using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class BigTimerController : MonoBehaviour
{
    float currentTime = 0f;
    float startingTime = 10f;
    bool counting = true;

    int code;
    public TextMeshProUGUI codeText;

    public TextMeshProUGUI timerText;

    void Start()
    {
        currentTime = startingTime;
    }

    void Update()
    {
        if (counting)
        {
            currentTime -= 1 * Time.deltaTime;
            timerText.text = ((int)currentTime / 60).ToString() + ":" + ((int)currentTime % 60).ToString();
            if (currentTime <= 0) TimesUp();
        }
        
    }

    void TimesUp()
    {
        gameObject.SendMessage("SendTimesUp");
        SceneManager.LoadScene("Start");
    }
}
