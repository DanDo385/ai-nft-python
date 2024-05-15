import { useState } from 'react';
import axios from 'axios';

const ImageGenerator = () => {
    const [prompt, setPrompt] = useState('');
    const [image, setImage] = useState(null);
    const [error, setError] = useState('');

    const generateImage = async () => {
        try {
            const response = await axios.post('http://localhost:5000/generate-image', { prompt });
            setImage(`data:image/png;base64,${response.data.image}`);
            setError('');
        } catch (error) {
            setError('Error generating image');
            console.error(error);
        }
    };

    return (
        <div>
            <h1>Generate Image with DALL-E 3</h1>
            <input
                type="text"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                placeholder="Enter prompt"
            />
            <button onClick={generateImage}>Generate Image</button>
            {image && <img src={image} alt="Generated" />}
            {error && <p>{error}</p>}
        </div>
    );
};

export default ImageGenerator;
