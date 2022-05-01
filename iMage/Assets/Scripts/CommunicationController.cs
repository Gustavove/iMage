using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class CommunicationController : MonoBehaviour
{
    public RawImage roundImage; 

    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine(GetTexture());
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    IEnumerator GetTexture()
    {
        UnityWebRequest www = UnityWebRequestTexture.GetTexture("https://source.unsplash.com/random");
        yield return www.SendWebRequest();

        if (www.result != UnityWebRequest.Result.Success)
        {
            Debug.Log(www.error);
        }
        else
        {
            Texture myTexture = ((DownloadHandlerTexture)www.downloadHandler).texture;
            roundImage.texture = myTexture;
            this.SendMessage("StartTimer");
        }
    }
}
