import React, { useState } from 'react';
import './yt.css';

function YoutubeInput() {
const [youtubeUrl, setYoutubeUrl] = useState('');
const [show, setShow] = useState('');
const [episode, setEpisode] = useState('');

const handleSubmit = async (event) => {
event.preventDefault();
try {
const response = await fetch('http://localhost:5000/', {
method: 'POST',
headers: {
'Accept': 'application/json',
'Content-Type': 'application/json'
},
body: JSON.stringify({url: youtubeUrl})
});

  if (response.ok) {
    const data = await response.json();
    setShow(data.show);
    setEpisode(data.episode);
    console.log('YouTube URL submitted successfully');
  } else {
    console.error('Failed to submit YouTube URL');
  }
} catch (error) {
  console.error('Failed to submit YouTube URL:', error);
}
}

const handleChange = (event) => {
setYoutubeUrl(event.target.value);
}

return (
<div className="form-wrapper">
<form onSubmit={handleSubmit} className="form-container">
<h1>Enter a YouTube URL</h1>
<div className="form-group">
<label htmlFor="youtubeUrl">YouTube URL:</label>
<input
         type="text"
         id="youtubeUrl"
         name="youtubeUrl"
         value={youtubeUrl}
         onChange={handleChange}
         placeholder="Enter the url"
         required
       />
</div>
<div className="result-container">
{show && <p>Show: {show}</p>}
{episode && <p>Episode: {episode}</p>}
</div>
<div className="form-group">
<button type="submit">Submit</button>

</div>

</form>
</div>
);
}

export default YoutubeInput;