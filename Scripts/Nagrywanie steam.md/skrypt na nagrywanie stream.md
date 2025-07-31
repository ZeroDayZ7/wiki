1. Nagrywanie filmów web gdy są streamowane z serwera. 

```script
const video = document.querySelector('video');
const stream = video.captureStream();
const recorder = new MediaRecorder(stream);
const chunks = [];

recorder.ondataavailable = e => chunks.push(e.data);
recorder.onstop = () => {
  const blob = new Blob(chunks, { type: 'video/webm' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'nagranie.webm';
  a.click();
};

recorder.start();

60 sekundach (zmień ile chcesz)
setTimeout(() => recorder.stop(), 60000);
```