# 🎵 Happy Voices Sing-Along! (Audio Version) 🎤

A Python-based singing app that uses pygame.mixer for audio playback, allowing you to listen to music while following the lyrics!

## 🚀 Features

- **Audio Playback**: Listen to music while singing along
- **Synchronized Lyrics**: Lyrics appear in time with the music
- **Personalized Experience**: Adjusts tempo based on user age
- **Multiple Genres**: Traditional nursery rhymes to modern pop songs
- **Interactive Interface**: Colorful console-based interface
- **Age-Appropriate Pacing**: Slower for younger kids, faster for older users

## 📋 Requirements

- Python 3.7 or higher
- pygame library
- Audio files (MP3, WAV, or OGG format)

## 🛠️ Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up audio files:**
   ```bash
   python download_audio_samples.py
   ```

3. **Add your audio files:**
   - Place audio files in the `audio_files` folder
   - Use the exact filenames specified in the app
   - Supported formats: MP3, WAV, OGG

## 🎵 Required Audio Files

Create or download these audio files and place them in the `audio_files` folder:

- `twinkle_twinkle.mp3` - Twinkle, Twinkle, Little Star
- `row_row_boat.mp3` - Row, Row, Row Your Boat
- `happy.mp3` - Happy (Kid Version)
- `cant_stop_feeling.mp3` - Can't Stop the Feeling (Kid Version)

## 🎼 Where to Get Audio Files

### Royalty-Free Music Sources:
- **Free Music Archive**: freemusicarchive.org
- **Incompetech**: incompetech.com
- **Bensound**: bensound.com
- **Pixabay Music**: pixabay.com/music/

### Tips for Audio Files:
- Use instrumental versions for best results
- Ensure files are in MP3, WAV, or OGG format
- Keep file sizes reasonable (under 10MB each)
- Test audio quality before using

## 🎯 How to Use

1. **Run the audio setup:**
   ```bash
   python download_audio_samples.py
   ```

2. **Add your audio files** to the `audio_files` folder

3. **Start the singing app:**
   ```bash
   python happy_voices_sing_along_audio.py
   ```

4. **Follow the prompts:**
   - Enter your name
   - Enter your age
   - Choose your favorite music genre
   - Select a song to sing

5. **Sing along!** 🎤
   - Audio will play automatically
   - Lyrics appear synchronized with the music
   - Get cheered on after each line

## 🎨 Features

### Age-Based Tempo Adjustment:
- **Under 5 years**: Slower pace for very young kids
- **5-7 years**: Medium pace for young kids
- **8-11 years**: Normal pace for older kids
- **12+ years**: Faster pace for teens and adults

### Genre Categories:
- **Nursery Rhymes**: Traditional children's songs
- **Pop Songs**: Modern kid-friendly hits
- **All Songs**: Complete collection

### Interactive Elements:
- **Colorful lyrics display**
- **Random encouraging cheers**
- **Personalized messages**
- **Progress tracking**

## 🔧 Customization

### Adding New Songs:
1. Edit the `songs` dictionary in `happy_voices_sing_along_audio.py`
2. Add your audio file to the `audio_files` folder
3. Update the `audio_file` field to match your filename

### Adjusting Tempo:
- Modify the `tempo` values in the songs dictionary
- Lower values = faster pace
- Higher values = slower pace

### Adding New Genres:
1. Update the genre filtering logic
2. Add new song categories
3. Update the user interface

## 🐛 Troubleshooting

### Audio Issues:
- **No sound**: Check if audio files exist and are valid
- **File not found**: Ensure audio files are in the correct folder
- **Format error**: Convert files to MP3, WAV, or OGG format

### Pygame Issues:
- **Import error**: Reinstall pygame: `pip install pygame`
- **Audio initialization**: Check system audio drivers
- **Permission error**: Run as administrator if needed

### General Issues:
- **Python version**: Ensure Python 3.7+ is installed
- **Dependencies**: Run `pip install -r requirements.txt`
- **File paths**: Use absolute paths if needed

## 📁 Project Structure

```
my_ai_jpurney/
├── happy_voices_sing_along_audio.py    # Main audio app
├── download_audio_samples.py           # Audio setup script
├── requirements.txt                    # Python dependencies
├── README_AUDIO.md                     # This file
├── audio_files/                        # Audio files folder
│   ├── twinkle_twinkle.mp3
│   ├── row_row_boat.mp3
│   ├── happy.mp3
│   └── cant_stop_feeling.mp3
└── midi_files/                         # MIDI files (optional)
```

## 🎵 Song List

### Traditional Songs:
- Twinkle, Twinkle, Little Star
- Row, Row, Row Your Boat

### Modern Songs (Kid Versions):
- Happy (Pharrell Williams)
- Can't Stop the Feeling (Justin Timberlake)

## 🤝 Contributing

To add more songs or features:
1. Fork the project
2. Add your audio files
3. Update the songs dictionary
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational purposes. Please ensure you have proper licenses for any audio files you use.

## 🎤 Happy Singing!

Enjoy your personalized singing experience with audio accompaniment! 🎵

---

**Note**: This version requires audio files to function properly. The app will work without audio files but will only display lyrics without music. 