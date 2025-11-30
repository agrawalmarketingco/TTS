// Minimal Service Worker – no caching, no offline support

self.addEventListener("install", () => {
  // Required event to activate the service worker
  self.skipWaiting();
});

self.addEventListener("activate", () => {
  // Ensures SW takes control immediately
  clients.claim();
});

// Optional fetch event (does nothing)
self.addEventListener("fetch", () => {
  // Empty on purpose – no caching, no interception
});
