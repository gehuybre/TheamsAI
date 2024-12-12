document.addEventListener('DOMContentLoaded', () => {
    console.log('AI Presentation Loaded');

    const videos = [
        {
            id: 'video1'
        },
        {
            id: 'video2'
        },
        {
            id: 'video3'
        }
    ];
    
    function requestFullScreen(element) {
        if (element.requestFullscreen) {
            element.requestFullscreen();
        } else if (element.mozRequestFullScreen) {
            element.mozRequestFullScreen();
        } else if (element.webkitRequestFullscreen) {
            element.webkitRequestFullscreen();
        } else if (element.msRequestFullscreen) {
            element.msRequestFullscreen();
        }
    }
    
    function initializeVideoPlayers() {
        videos.forEach(videoConfig => {
            const video = document.getElementById(videoConfig.id);
            
            if (video) {
                // Set initial properties
                video.muted = true;
                video.controls = false; // Hide video controls
                
                // Reset and play video when slide becomes active
                Reveal.on('slidechanged', (event) => {
                    const slideElement = event.currentSlide;
                    const videoElement = slideElement.querySelector(`#${videoConfig.id}`);
                    
                    if (videoElement) {
                        videoElement.currentTime = 0;
                        videoElement.play();
                        /* Set playback speed only for video3 */
                        if (videoConfig.id === 'video3') {
                            videoElement.playbackRate = 0.4;
                        } else {
                            videoElement.playbackRate = 1.0; // Normal speed for other videos
                        }
                    }
                });
    
                // Pause video when leaving slide
                Reveal.on('slidechanged', (event) => {
                    const previousSlide = event.previousSlide;
                    if (previousSlide) {
                        const prevVideo = previousSlide.querySelector(`#${videoConfig.id}`);
                        if (prevVideo) {
                            prevVideo.pause();
                            prevVideo.currentTime = 0;
                        }
                    }
                });
    
                // Handle video end
                video.addEventListener('ended', () => {
                    video.pause();
                });
            }
        });
    }
    
    initializeVideoPlayers();

    function initializeAudioPlayers() {
        const audio = document.getElementById('audio1');
        
        if (audio) {
            audio.muted = false;
            audio.controls = false; // Hide audio controls

            Reveal.on('slidechanged', (event) => {
                const currentSlide = event.currentSlide;
                if (currentSlide.querySelector('#audio1')) {
                    audio.currentTime = 0;
                    audio.play();
                } else {
                    audio.pause();
                    audio.currentTime = 0;
                }
            });
        }
    }

    initializeAudioPlayers();
});