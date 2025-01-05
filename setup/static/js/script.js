//*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
//*-*-*-*-*-*-*-*-*HEADER*-*-*-*-*-*-*-*-*

document.addEventListener('DOMContentLoaded', function() {
    // Código para dropdowns
    const menuItems = document.querySelectorAll('.menu-item');
    const dropdowns = document.querySelectorAll('.dropdown');

    // Garante que todos os dropdowns estão escondidos quando a página carrega
    dropdowns.forEach(dropdown => {
        dropdown.style.display = 'none';
    });

    menuItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            const dropdown = this.querySelector('.dropdown');
            if (dropdown) {
                dropdown.style.display = 'block';
            }
        });

        item.addEventListener('mouseleave', function() {
            const dropdown = this.querySelector('.dropdown');
            if (dropdown) {
                dropdown.style.display = 'none';
            }
        });
    });


//*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
//*-*-*-*-*-*-*-*-*MEUS PEDIDOS*-*-*-*-*-*-*-*-*

    // Função para alterar o texto do botão com base na seleção
    window.selectYear = function(element) {
        // Obtém o texto do item selecionado
        var selectedYear = element.textContent;
        // Define o texto do botão para o ano selecionado
        document.getElementById('dropdownMenuButton').textContent = selectedYear;
        document.getElementById('anoSelecionado').value = selectedYear;
        // Submete o formulário automaticamente
        document.getElementById('formFiltroAno').submit();
    };



//*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
//*-*-*-*-*-*-*-*ALTERAR SENHA*-*-*-*-*-*-*-*

// Código para validar as senhas e habilitar/desabilitar o botão
const currentPassword = document.getElementById('currentPassword');
const newPassword = document.getElementById('newPassword');
const confirmPassword = document.getElementById('confirmPassword');
const passwordFeedback = document.getElementById('passwordFeedback');
const submitButton = document.getElementById('submitButton');
const alertsDiv = document.getElementById('alertas-senhas');

// Função para validar a força da senha e atualizar os requisitos
function updatePasswordAlerts(password) {
    const lengthRequirement = document.getElementById('lengthRequirement');
    const uppercaseRequirement = document.getElementById('uppercaseRequirement');
    const lowercaseRequirement = document.getElementById('lowercaseRequirement');
    const numberRequirement = document.getElementById('numberRequirement');
    const specialCharRequirement = document.getElementById('specialCharRequirement');
    
    // Validações para cada critério
    const lengthValid = password.length >= 8;
    const uppercaseValid = /[A-Z]/.test(password);
    const lowercaseValid = /[a-z]/.test(password);
    const numberValid = /\d/.test(password);
    const specialCharValid = /[\W_]/.test(password);

    // Atualiza a cor dos requisitos (verde se atendido, vermelho caso contrário)
    lengthRequirement.style.color = lengthValid ? 'green' : 'red';
    uppercaseRequirement.style.color = uppercaseValid ? 'green' : 'red';
    lowercaseRequirement.style.color = lowercaseValid ? 'green' : 'red';
    numberRequirement.style.color = numberValid ? 'green' : 'red';
    specialCharRequirement.style.color = specialCharValid ? 'green' : 'red';
}

// Função para validar a força da senha
function isPasswordStrong(password) {
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;
    return regex.test(password);
}

function validatePasswords() {
    const allFilled = currentPassword.value !== '' && newPassword.value !== '' && confirmPassword.value !== '';

    // Atualiza os alertas da senha
    updatePasswordAlerts(newPassword.value);

    if (newPassword.value !== confirmPassword.value) {
        passwordFeedback.textContent = "As senhas não coincidem.";
        passwordFeedback.style.color = "red";
        submitButton.disabled = true;
    } else if (!isPasswordStrong(newPassword.value)) {
        passwordFeedback.textContent = "A nova senha não atende aos requisitos.";
        passwordFeedback.style.color = "red";
        submitButton.disabled = true;
    } else {
        passwordFeedback.textContent = '';
    }

    submitButton.disabled = !allFilled || (newPassword.value !== confirmPassword.value) || !isPasswordStrong(newPassword.value);
}

if (currentPassword && newPassword && confirmPassword && passwordFeedback && submitButton) {
    currentPassword.addEventListener('input', validatePasswords);
    newPassword.addEventListener('input', validatePasswords);
    confirmPassword.addEventListener('input', validatePasswords);
}

//*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
//*-*-*-*-*-*-*-*-*MEU CADASTRO*-*-*-*-*-*-*-*-*
const cepInput = document.getElementById('cep');
if (cepInput) {
    cepInput.addEventListener('input', function(e) {
        let cep = e.target.value.replace(/\D/g, '');
        cep = cep.replace(/(\d{5})(\d{3})$/, "$1-$2"); // Coloca o traço
        e.target.value = cep;
    });
}

const cpfInput = document.getElementById('cpf');
if (cpfInput) {
    cpfInput.addEventListener('input', function(e) {
        let cpf = e.target.value.replace(/\D/g, ''); // Remove todos os não-dígitos
        cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2");   // Coloca o primeiro ponto
        cpf = cpf.replace(/(\d{3})(\d)/, "$1.$2");   // Coloca o segundo ponto
        cpf = cpf.replace(/(\d{3})(\d{1,2})$/, "$1-$2"); // Coloca o traço
        e.target.value = cpf;
    });
}

const telefoneInput = document.getElementById('telefone');
if (telefoneInput) {
    telefoneInput.addEventListener('input', function(e) {
        let telefone = e.target.value.replace(/\D/g, ''); // Remove todos os não-dígitos
        telefone = telefone.replace(/^(\d{2})(\d)/g, "($1) $2"); // Coloca parênteses no DDD
        telefone = telefone.replace(/(\d{5})(\d)/, "$1-$2"); // Coloca o traço no número
        e.target.value = telefone;
    });
}

const titleUser = document.getElementById('titulo-usuario');
const userInfoName = document.getElementById('userInfo-nome');
const userInfoLastName = document.getElementById('userInfo-sobrenome');
const userInfoCPF = document.getElementById('userInfo-cpf');
const userInfoEmail = document.getElementById('userInfo-email');
const userInfoBirth = document.getElementById('userInfo-birth');
const userInfoPhone = document.getElementById('userInfo-phone');
const saveCancelButtons = document.getElementById('btnsSaveCancel');
//mudar classe
const cancelBtn = document.getElementById('cancel-btn');
const saveBtn = document.getElementById('save-btn');
const editBtn = document.getElementById('edit-btn');
//botões de submissão
const nameView = document.getElementById('nome-view');
const lastNameView = document.getElementById('sobrenome-view');
const cpfView = document.getElementById('cpf-view');
const emailView = document.getElementById('email-view');
const birthView = document.getElementById('birth-view');
const phoneView = document.getElementById('phone-view');
const nameEdit = document.getElementById('nome-edit');
const lastNameEdit = document.getElementById('sobrenome-edit');
const cpfEdit = document.getElementById('cpf');
const emailEdit = document.getElementById('email-edit');
const birthEdit = document.getElementById('birth-edit');
const phoneEdit = document.getElementById('telefone');

editBtn.addEventListener('click', () => {
    titleUser.classList.remove('view-mode');
    titleUser.classList.add('edit-mode');

    // 
    userInfoName.classList.remove('view-mode');
    userInfoName.classList.add('edit-mode');

    userInfoLastName.classList.remove('view-mode');
    userInfoLastName.classList.add('edit-mode');

    userInfoCPF.classList.remove('view-mode');
    userInfoCPF.classList.add('edit-mode');

    userInfoEmail.classList.remove('view-mode');
    userInfoEmail.classList.add('edit-mode');

    userInfoBirth.classList.remove('view-mode');
    userInfoBirth.classList.add('edit-mode');

    userInfoPhone.classList.remove('view-mode');
    userInfoPhone.classList.add('edit-mode');
    // 

    saveCancelButtons.classList.remove('view-mode');
    saveCancelButtons.classList.add('edit-mode');
});

saveBtn.addEventListener('click', () => {
    nameView.textContent = nameEdit.value;
    lastNameView.textContent = lastNameEdit.value;
    cpfView.textContent = cpfEdit.value;
    emailView.textContent = emailEdit.value;
    birthView.textContent = birthEdit.value;
    phoneView.textContent = phoneEdit.value;

    titleUser.classList.remove('edit-mode');
    titleUser.classList.add('view-mode');

    // 
    userInfoName.classList.remove('edit-mode');
    userInfoName.classList.add('view-mode');

    userInfoLastName.classList.remove('edit-mode');
    userInfoLastName.classList.add('view-mode');

    userInfoCPF.classList.remove('edit-mode');
    userInfoCPF.classList.add('view-mode');

    userInfoEmail.classList.remove('edit-mode');
    userInfoEmail.classList.add('view-mode');

    userInfoBirth.classList.remove('edit-mode');
    userInfoBirth.classList.add('view-mode');

    userInfoPhone.classList.remove('edit-mode');
    userInfoPhone.classList.add('view-mode');
    // 

    saveCancelButtons.classList.remove('edit-mode');
    saveCancelButtons.classList.add('view-mode');

    // Aplicar lógica para verificar se o bd foi atualizado com sucesso!!!
    alert("Alterações realizadas com sucesso!")

});

cancelBtn.addEventListener('click', () => {
    // Aplicar lógica para perguntar se a pessoa tem certeza de que quer descartar as alterações
    
    titleUser.classList.remove('edit-mode');
    titleUser.classList.add('view-mode');

    userInfo.classList.remove('edit-mode');
    userInfo.classList.add('view-mode');

    // 
    userInfoName.classList.remove('edit-mode');
    userInfoName.classList.add('view-mode');

    userInfoLastName.classList.remove('edit-mode');
    userInfoLastName.classList.add('view-mode');

    userInfoCPF.classList.remove('edit-mode');
    userInfoCPF.classList.add('view-mode');

    userInfoEmail.classList.remove('edit-mode');
    userInfoEmail.classList.add('view-mode');

    userInfoBirth.classList.remove('edit-mode');
    userInfoBirth.classList.add('view-mode');

    userInfoPhone.classList.remove('edit-mode');
    userInfoPhone.classList.add('view-mode');
    // 

    saveCancelButtons.classList.remove('edit-mode');
    saveCancelButtons.classList.add('view-mode');
});


//*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
// *-*-*-*-*-*-*-*-*-*CATALOGO*-*-*-*-*-*-*-*-*

const dropdownButtonUnique = document.getElementById('dropdownButtonUnique');
const dropdownItemsUnique = document.querySelectorAll('#dropdownMenuUnique .dropdown-item');

// Adiciona um event listener aos itens do dropdown específico
dropdownItemsUnique.forEach(item => {
    item.addEventListener('click', function(event) {
        event.preventDefault();  // Previne comportamento padrão do link
        dropdownButtonUnique.textContent = this.textContent;  // Atualiza o texto do botão com o item clicado
    });
});

//BREADCRUMB NÃO ESTÁ FUNCIONANDO DIREITO
// Função para adicionar um item ao breadcrumb
function addBreadcrumb(name, url) {
    const breadcrumbList = document.getElementById('breadcrumb-list');
    
    // Cria um novo item de breadcrumb
    const newItem = document.createElement('li');
    newItem.className = 'breadcrumb-item';

    if (url) {
        // Se houver URL, cria um link
        const link = document.createElement('a');
        link.href = url;
        link.textContent = name;
        newItem.appendChild(link);
    } else {
        // Se não houver URL, é o item ativo
        newItem.classList.add('active');
        newItem.setAttribute('aria-current', 'page');
        newItem.textContent = name;
    }

    // Adiciona o novo item à lista de breadcrumbs
    breadcrumbList.appendChild(newItem);
}

// Exemplo de uso da função
addBreadcrumb('Library', '/library');
addBreadcrumb('Data', '/library/data');
  
})

// xxxxxxxxxxxxxx adicionar e retirar filtro xxxxxxxxxxxxxx
// $(document).ready(function() {
//     // Função chamada ao selecionar/desmarcar um filtro
//     $('.filtro').on('change', function() {
//       var filtro = $(this).val();
//       var isChecked = $(this).is(':checked');

//       if (isChecked) {
//         adicionarFiltro(filtro, this);
//       } else {
//         removerFiltro(filtro);
//       }
//     });

//     // Função para adicionar o botão do filtro aplicado
//     function adicionarFiltro(filtro, checkboxElement) {
//       // Verifica se o botão já não foi adicionado
//       if (!$(`.filtro-btn[data-filtro="${filtro}"]`).length) {
//         $('.filtros-aplicados').append(`
//           <button class="filtro-btn" data-filtro="${filtro}">${filtro} &times;</button>
//         `);

//         // Associa o evento de remoção ao botão
//         $(`.filtro-btn[data-filtro="${filtro}"]`).on('click', function() {
//           $(this).remove(); // Remove o botão
//           $(checkboxElement).prop('checked', false); // Desmarca o checkbox correspondente
//         });
//       }
//     }

//     // Função para remover o botão do filtro aplicado
//     function removerFiltro(filtro) {
//       $(`.filtro-btn[data-filtro="${filtro}"]`).remove();
//     }
// });

$(document).ready(function() {
    // Função chamada ao selecionar/desmarcar um filtro
    $('.filtro').on('change', function() {
      var filtro = $(this).val();
      var isChecked = $(this).is(':checked');

      if (isChecked) {
        adicionarFiltro(filtro, this);
      } else {
        removerFiltro(filtro);
      }

      verificarFiltros();
    });

    // Função para adicionar o botão do filtro aplicado
    function adicionarFiltro(filtro, checkboxElement) {
      // Verifica se o botão já não foi adicionado
      if (!$(`.filtro-btn[data-filtro="${filtro}"]`).length) {
        $('.filtros-aplicados').append(`
          <button class="filtro-btn" data-filtro="${filtro}">${filtro} &times;</button>
        `);

        // Associa o evento de remoção ao botão
        $(`.filtro-btn[data-filtro="${filtro}"]`).on('click', function() {
          $(this).remove(); // Remove o botão
          $(checkboxElement).prop('checked', false); // Desmarca o checkbox correspondente
          verificarFiltros();
        });
      }
    }

    // Função para remover o botão do filtro aplicado
    function removerFiltro(filtro) {
      $(`.filtro-btn[data-filtro="${filtro}"]`).remove();
    }

    // Verifica se há filtros ativos e exibe/esconde a mensagem
    function verificarFiltros() {
        if ($('.filtro:checked').length > 0) {
          $('#limpar-filtros').show(); // Mostra o botão "Limpar Filtros"
          $('.selecao-filtros').show(); // Mostra a div de seleção de filtros
        } else {
          $('#limpar-filtros').hide(); // Esconde o botão "Limpar Filtros"
          $('.selecao-filtros').hide(); // Oculta a div de seleção de filtros
        }
      }

    // Função para limpar todos os filtros
    $('#limpar-filtros').on('click', function() {
      $('.filtro').prop('checked', false); // Desmarca todas as checkboxes
      $('.filtro-btn').remove(); // Remove todos os botões de filtro
      verificarFiltros(); // Atualiza a interface
    });

    // Inicialização: Verifica se algum filtro já está selecionado
    verificarFiltros();
});

//*-*-*-*-*-*-*-*-*-*-*-*-*CARRINHO*-*-*-*-*-*-*-*-*-*-*-*-*
document.addEventListener('DOMContentLoaded', function() {
    const cartIcon = document.getElementById('cartIcon');
    const cartPopup = document.getElementById('cartPopup');
    const cartItems = document.getElementById('cartItems');
    const cartFilled = document.getElementById('cartFilled');
    const cartEmpty = document.getElementById('cartEmpty');
    const badgeCart = document.getElementById('badgeCart');
  
    // Função para abrir o pop-up ao passar o mouse no ícone
    cartIcon.addEventListener('mouseover', () => {
        cartPopup.classList.add('active');
    });

    // Função para fechar o pop-up ao tirar o mouse do ícone e do pop-up
    cartIcon.addEventListener('mouseout', (event) => {
        if (!cartPopup.contains(event.relatedTarget)) {
            cartPopup.classList.remove('active');
        }
    });
  
    // Permite que o popup continue visível ao passar o mouse sobre ele
    cartPopup.addEventListener('mouseover', () => {
        cartPopup.classList.add('active');
    });

    cartPopup.addEventListener('mouseout', (event) => {
        if (!cartIcon.contains(event.relatedTarget)) {
            cartPopup.classList.remove('active');
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const loggedBtn = document.getElementById('loggedBtn');
    const popupUserOptions = document.getElementById('popupUserOptions');
  
    // Função para abrir o pop-up ao passar o mouse no ícone
    loggedBtn.addEventListener('mouseover', () => {
        popupUserOptions.classList.add('active');
    });

    // Função para fechar o pop-up ao tirar o mouse do ícone e do pop-up
    loggedBtn.addEventListener('mouseout', (event) => {
        if (!popupUserOptions.contains(event.relatedTarget)) {
            popupUserOptions.classList.remove('active');
        }
    });
  
    // Permite que o popup continue visível ao passar o mouse sobre ele
    popupUserOptions.addEventListener('mouseover', () => {
        popupUserOptions.classList.add('active');
    });

    popupUserOptions.addEventListener('mouseout', (event) => {
        if (!cartIcon.contains(event.relatedTarget)) {
            popupUserOptions.classList.remove('active');
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const cardNumber = document.getElementById('card-number');
    const cardName = document.getElementById('card-name');
    const cardExpiry = document.getElementById('card-expiry');
    const cardCvv = document.getElementById('card-cvv');
    const card = document.getElementById('card');

    const cvvInput = document.getElementById('cvv');
    const numberInput = document.getElementById('NCartao');
    const nameInput = document.getElementById('Nome');
    const expiryInput = document.getElementById('dataExp');

    const creditCardNumber = document.querySelector('card-number');
    const creditCardCvv = document.querySelector('card-cvv');
    const creditCardInner = document.querySelector('.card-inner');
    const creditCardCvvElement = document.querySelector('cvv');

    creditCardCvv.addEventListener('focus', () => {
    creditCardInner.classList.add("card-flip");
    })

    creditCardCvv.addEventListener("focusout", () => {
    creditCardInner.classList.remove("card-flip");
    });

    creditCardNumber.addEventListener('input', event => {
    if (isNaN(Number(event.target.value))) {
        event.target.value = event.target.value.substr(0, event.target.value.length - 1);
        return;
    }

    let cardNumber = [];
    if (event.target.value.length > 0) {
        cardNumber = event.target.value.match(/[0-9]{1,4}/g);
    } 

    const cardNo1 = document.querySelector('#cardNo1');
    const cardNo2 = document.querySelector('#cardNo2');
    const cardNo3 = document.querySelector('#cardNo3');
    const cardNo4 = document.querySelector('#cardNo4');

    cardNo1.textContent = cardNumber[0] ?? '1234';
    cardNo2.textContent = cardNumber[1] ?? '5678';
    cardNo3.textContent = cardNumber[2] ?? '9012';
    cardNo4.textContent = cardNumber[3] ?? '3456';

    if (event.target.value.length === 17) {
        event.target.value = event.target.value.substr(
            0,
            event.target.value.length - 1
        );
    }

    })

    creditCardCvv.addEventListener('input', event => {
    if (isNaN(Number(event.target.value))) {
        event.target.value = event.target.value.substr(
        0,
        event.target.value.length - 1
        );
        return;
    }

        if (event.target.value.length === 0) {
        creditCardCvvElement.textContent = 123;
        return;
        }
    
    
    if (event.target.value.length === 4) {
        event.target.value = event.target.value.substr(
        0,
        event.target.value.length - 1
        );
        return;
    }

    creditCardCvvElement.textContent = event.target.value;
    })


    
    numberInput.addEventListener('input', function () {
        const value = this.value.replace(/\s+/g, '').replace(/(.{4})/g, '$1 ').trim();
        cardNumber.textContent = value || '**** **** **** ****';
    });
    
    nameInput.addEventListener('input', function () {
        cardName.textContent = this.value || 'John Doe';
    });
    
    expiryInput.addEventListener('input', function () {
        cardExpiry.textContent = this.value || 'MM/YY';
    });

    document.addEventListener('DOMContentLoaded', function () {


    cvvInput.addEventListener('focus', function () {
        card.classList.add('flip');
    });
    
    cvvInput.addEventListener('blur', function () {
        card.classList.remove('flip');
    });
    
    cvvInput.addEventListener('input', function () {
        cardCvv.textContent = this.value || '***';
    });
});
})

document.addEventListener('DOMContentLoaded', function() {
    // Seleciona todos os controles de quantidade
    const qtdControls = document.querySelectorAll('.secao-quantidade-pag-produto');
    
    // Itera sobre cada conjunto de controles
    qtdControls.forEach(function(control) {
        const decreaseButton = control.querySelector('.decrease-btn');
        const increaseButton = control.querySelector('.increase-btn');
        const quantityInput = control.querySelector('.qtd-produto-pagina');
        
        // Função para atualizar o valor do input
        function updateQuantity(amount) {
            const currentValue = parseInt(quantityInput.value, 10);
            const minValue = parseInt(quantityInput.min, 10);
            const maxValue = parseInt(quantityInput.max, 10);
            
            let newValue = currentValue + amount;
            
            // Garante que o valor não fique abaixo do mínimo ou acima do máximo
            if (newValue < minValue) {
                newValue = minValue;
            }
            if (newValue > maxValue) {
                newValue = maxValue;
            }
            
            quantityInput.value = newValue;
        }
        
        // Adiciona event listeners para os botões
        decreaseButton.addEventListener('click', function() {
            updateQuantity(-1);
        });
        
        increaseButton.addEventListener('click', function() {
            updateQuantity(1);
        });
    });
});


