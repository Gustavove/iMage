using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;
using Newtonsoft.Json.Linq;

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
            myTexture.wrapMode = TextureWrapMode.Clamp;
            roundImage.texture = myTexture;
            this.SendMessage("StartTimer");
        }
    }


    IEnumerator PostData_Coroutine(string n)
    {
        string uri = "http://localhost:5000/crea_partida";
        WWWForm form = new WWWForm();
        form.AddField("nick",n);
        using (UnityWebRequest request = UnityWebRequest.Post(uri, form))
        {
            yield return request.SendWebRequest();
            if (request.isNetworkError || request.isHttpError)
                Debug.Log(request.error);
            else
            {
                string s = request.downloadHandler.text;
                int x = 0;
                char[] ch = new char[s.Length];
                for (int i = 7; i < s.Length; i++)
                {
                    ch[x] = s[i];
                    ++x;
                }
                Debug.Log(s);
            }
                
        }
    }
}
