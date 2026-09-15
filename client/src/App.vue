<script setup>
import { onMounted, ref } from "vue";

// One template literal: Vite replaces the env ref at transform time and the
// bundler folds it into a single contiguous string (required by the proof gate).
const frontendLine = `frontend: hello world oxzoo-vue-django_${import.meta.env.GREETING_TAG}`;

const backendLine = ref("");
const errorMessage = ref("");
const loading = ref(true);

onMounted(async () => {
  try {
    const response = await fetch("/api/greeting");
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    backendLine.value = `backend: ${await response.text()}`;
  } catch (error) {
    errorMessage.value = error.message;
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <main>
    <h1>oxzoo-vue-django</h1>
    <p><strong>{{ frontendLine }}</strong></p>
    <p v-if="loading">backend: loading&hellip;</p>
    <p v-else-if="errorMessage" class="error">backend: request failed ({{ errorMessage }})</p>
    <p v-else><strong>{{ backendLine }}</strong></p>
  </main>
</template>

<style>
body {
  font-family: system-ui, sans-serif;
  margin: 2rem;
  background: #fafafa;
  color: #1a1a1a;
}

h1 {
  font-size: 1.5rem;
}

p {
  margin: 0.5rem 0;
}

.error {
  color: #b3261e;
}
</style>
