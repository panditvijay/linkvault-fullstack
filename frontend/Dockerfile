# ---- Stage 1: Build the React App ----
# Use a Node.js image to get npm
FROM node:20-alpine AS build

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the application for production
RUN npm run build

# ---- Stage 2: Serve the built app with Nginx ----
# Use a lightweight Nginx image
FROM nginx:1.21-alpine

# Copy the static files from the build stage
# The 'npm run build' command creates a 'dist' folder
COPY --from=build /app/dist /usr/share/nginx/html

# Nginx will automatically serve the index.html from this folder

# Expose port 80
EXPOSE 80

# The default command for the nginx image is to start the server,
# so we don't need a CMD instruction.