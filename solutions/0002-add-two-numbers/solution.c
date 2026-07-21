/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) 
{
    struct ListNode *dummy = (struct ListNode *)malloc(sizeof(struct ListNode));
    dummy->next = NULL;

    struct ListNode *curr = dummy;

    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry) {

        int x = (l1 != NULL) ? l1->val : 0;
        int y = (l2 != NULL) ? l2->val : 0;

        int sum = x + y + carry;

        carry = sum / 10;

        struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
        node->val = sum % 10;
        node->next = NULL;

        curr->next = node;
        curr = curr->next;

        if (l1 != NULL)
            l1 = l1->next;

        if (l2 != NULL)
            l2 = l2->next;
    }

    return dummy->next;

    
}
