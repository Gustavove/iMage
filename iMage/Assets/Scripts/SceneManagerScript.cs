using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneManagerScript : MonoBehaviour
{

    private string nickname;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    
    public void LoadScene(string sceneName){
    	SceneManager.LoadScene(sceneName);
    }

    public void CreateGame()
    {
        if (nickname != null)
        {
            SceneManager.LoadScene("CreateGame");
        }
    }

    public void JoinGame()
    {
        if (nickname != null)
        {
            SceneManager.LoadScene("JoinGame");
        }
    }

    public void ReadStringInput(string s)
    {
        nickname=s;
    }
}
