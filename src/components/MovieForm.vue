<template>
  <div>
    <!-- Movie form HTML code goes here -->
    <form id="movieForm" @submit.prevent="saveMovie">
      <!-- Your form fields here -->
      <button type="submit">Save Movie</button>
    </form>
    
    <!-- Display success message if successful upload -->
    <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
    </div>
    
    <!-- Display error messages if validation fails -->
    <div v-if="errorMessages.length > 0" class="alert alert-danger">
      <ul>
        <li v-for="error in errorMessages" :key="error">{{ error }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    let csrf_token = ref("");
    let successMessage = ref("");
    let errorMessages = ref([]);

    function getCsrfToken() {
      fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          csrf_token.value = data.csrf_token;
        });
    }

    onMounted(() => {
      getCsrfToken();
    });

    function saveMovie() {
      let movieForm = document.getElementById('movieForm');
      let form_data = new FormData(movieForm);
      fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
          'X-CSRFToken': csrf_token.value
        }
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          // Display success message
          successMessage.value = 'Movie uploaded successfully!';
          errorMessages.value = []; // Clear error messages
        })
        .catch(function (error) {
          console.log(error);
          // Display error message
          errorMessages.value = ['An error occurred. Please try again later.'];
          successMessage.value = ''; // Clear success message
        });
    }

    return {
      csrf_token,
      successMessage,
      errorMessages,
      saveMovie
    };
  }
}
</script>
