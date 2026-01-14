using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Security.Cryptography;
using System;
using System.Collections.Generic;

public class NeuroSyncReceiver : MonoBehaviour
{
    // --- CONFIGURATION ---
    public int port = 5065;
    private string aesKey = "1234567890123456"; // Must match Python Key

    // --- VARIABLES ---
    Thread receiveThread;
    UdpClient client;
    public float currentFlex = 0;
    public bool isFatigued = false;
    
    // For visuals
    public Transform fingerJoint; // Assign a part of your 3D model here
    
    void Start()
    {
        receiveThread = new Thread(new ThreadStart(ReceiveData));
        receiveThread.IsBackground = true;
        receiveThread.Start();
        Debug.Log("Unity Listening on Port " + port);
    }

    private void ReceiveData()
    {
        client = new UdpClient(port);
        while (true)
        {
            try
            {
                IPEndPoint anyIP = new IPEndPoint(IPAddress.Any, 0);
                byte[] data = client.Receive(ref anyIP);
                string encryptedText = Encoding.UTF8.GetString(data);

                // 1. DECRYPT
                string jsonText = Decrypt(encryptedText, aesKey);
                
                // 2. PARSE JSON (Simple manual parsing for speed)
                // Expected format: {"flex": 50, "fatigue": false}
                if (jsonText.Contains("flex"))
                {
                    // Extract Flex
                    int flexIndex = jsonText.IndexOf("flex") + 6;
                    int commaIndex = jsonText.IndexOf(",");
                    string flexStr = jsonText.Substring(flexIndex, commaIndex - flexIndex);
                    currentFlex = float.Parse(flexStr);

                    // Extract Fatigue
                    isFatigued = jsonText.Contains("true");
                }
            }
            catch (Exception err)
            {
                Debug.LogError(err.ToString());
            }
        }
    }

    void Update()
    {
        // --- VISUALIZATION ---
        
        // 1. Rotate the finger based on Flex Value
        // Assuming X-axis rotation is the bending motion
        float angle = Mathf.Lerp(0, 90, currentFlex / 100f); 
        if(fingerJoint != null)
        {
            fingerJoint.localRotation = Quaternion.Euler(angle, 0, 0);
        }
        else 
        {
             // Fallback: Just rotate the cube
             transform.rotation = Quaternion.Euler(angle, 0, 0);
        }

        // 2. Show Fatigue Status
        if (isFatigued)
        {
            GetComponent<Renderer>().material.color = Color.red; // Alert Color
        }
        else
        {
            GetComponent<Renderer>().material.color = Color.green; // Normal Color
        }
    }

    // --- DECRYPTION LOGIC ---
    public string Decrypt(string cipherText, string key)
    {
        byte[] cipherBytes = Convert.FromBase64String(cipherText);
        using (Aes aesAlg = Aes.Create())
        {
            aesAlg.Key = Encoding.UTF8.GetBytes(key);
            aesAlg.Mode = CipherMode.ECB; // Matching Python
            aesAlg.Padding = PaddingMode.PKCS7;
            
            ICryptoTransform decryptor = aesAlg.CreateDecryptor(aesAlg.Key, aesAlg.IV);
            byte[] decryptedBytes = decryptor.TransformFinalBlock(cipherBytes, 0, cipherBytes.Length);
            return Encoding.UTF8.GetString(decryptedBytes);
        }
    }

    void OnApplicationQuit()
    {
        if (receiveThread != null) receiveThread.Abort();
        client.Close();
    }
}