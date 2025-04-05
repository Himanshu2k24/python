// main.js - JavaScript for Campus Bites Food Delivery Application

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Handle quantity adjustments in cart
    const quantityInputs = document.querySelectorAll('.quantity-form input[type="number"]');
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            // Auto-submit the form when quantity changes
            this.closest('form').submit();
        });
    });

    // Checkout page - Toggle delivery options
    const deliveryOptions = document.querySelectorAll('input[name="delivery_option"]');
    const locationFields = document.querySelectorAll('#building, #room');
    
    if (deliveryOptions.length) {
        deliveryOptions.forEach(option => {
            option.addEventListener('change', function() {
                if (this.value === 'pickup') {
                    locationFields.forEach(field => {
                        field.required = false;
                        field.closest('.row').style.opacity = '0.5';
                    });
                } else {
                    locationFields.forEach(field => {
                        field.required = true;
                        field.closest('.row').style.opacity = '1';
                    });
                }
            });
        });
    }

    // Add to cart animation
    const addToCartBtns = document.querySelectorAll('button[type="submit"]');
    addToCartBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Add a simple animation when adding to cart
            this.innerHTML = '<i class="fas fa-check"></i> Added';
            this.classList.remove('btn-primary');
            this.classList.add('btn-success');
            
            // Reset after 1 second
            setTimeout(() => {
                this.innerHTML = '<i class="fas fa-cart-plus me-1"></i> Add';
                this.classList.remove('btn-success');
                this.classList.add('btn-primary');
            }, 1000);
        });
    });

    // Order tracking animation
    const checkIcon = document.querySelector('.fa-check-circle');
    if (checkIcon) {
        checkIcon.classList.add('order-success-icon');
    }
});