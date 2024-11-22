// custom.js
document.addEventListener('DOMContentLoaded', () => {
    console.log('AI Presentation Loaded');
});

// Ensure the script runs after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
    let players = {};

    // Configuration for each video
    const videos = [
        {
            id: 'youtube-player-1',
            videoId: 'LPZh9BOjkQs', // Replace with your first YouTube video ID
            startSeconds: 81,
            endSeconds: 92
        },
        {
            id: 'youtube-player-2',
            videoId: 'LPZh9BOjkQs', // Replace with your second YouTube video ID
            startSeconds: 60,
            endSeconds: 75
        },
        // Add more video configurations as needed
    ];

    // Function to load the YouTube IFrame API
    function loadYouTubeAPI(callback) {
        // Check if the API is already loaded
        if (window.YT && window.YT.Player) {
            callback();
        } else {
            // Create a script tag to load the YouTube IFrame API
            let tag = document.createElement('script');
            tag.src = "https://www.youtube.com/iframe_api";
            let firstScriptTag = document.getElementsByTagName('script')[0];
            firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

            // Define the callback for when the API is ready
            window.onYouTubeIframeAPIReady = callback;
        }
    }

    // Request full screen for a given element
    function requestFullScreen(element) {
        if (element.requestFullscreen) {
            element.requestFullscreen();
        } else if (element.mozRequestFullScreen) { // Firefox
            element.mozRequestFullScreen();
        } else if (element.webkitRequestFullscreen) { // Chrome, Safari and Opera
            element.webkitRequestFullscreen();
        } else if (element.msRequestFullscreen) { // IE/Edge
            element.msRequestFullscreen();
        }
    }

    // Initialize YouTube Players
    function initializeYouTubePlayers() {
        videos.forEach(video => {
            players[video.id] = new YT.Player(video.id, {
                height: window.innerHeight,
                width: window.innerWidth,
                videoId: video.videoId,
                playerVars: {
                    'autoplay': 1,
                    'controls': 0,
                    'start': video.startSeconds,
                    'end': video.endSeconds,
                    'mute': 1, // Mute the video
                    'rel': 0, // Do not show related videos
                    'showinfo': 0, // Do not show video info
                    'modestbranding': 1, // Minimal YouTube branding
                    'iv_load_policy': 3, // Do not show video annotations
                    'fs': 1, // Allow fullscreen
                    'playsinline': 1, // Play inline on mobile devices
                    'vq': 'hd720' // Play video in 720p
                },
                events: {
                    'onReady': (event) => {
                        event.target.playVideo();
                        event.target.mute(); // Ensure the video is muted
                        requestFullScreen(event.target.getIframe());
                    },
                    'onStateChange': (event) => {
                        if (event.data === YT.PlayerState.ENDED) {
                            // Seek to the last second and pause to freeze the frame
                            event.target.seekTo(video.endSeconds - 0.1, true);
                            event.target.pauseVideo();
                        }
                    }
                }
            });
        });
    }

    // Load the YouTube IFrame API and initialize players
    loadYouTubeAPI(initializeYouTubePlayers);
});
